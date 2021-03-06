from django.http import JsonResponse
from rest_framework import viewsets
from PlagiarismChecker.checker import PlagCheck
from OCR.prediction import inference_web


class PlagCheckViewSet(viewsets.ViewSet):
    def check_plagiarism(self, request):
        if request.data["mode"] == "text" and "text" in request.data.keys():
            text = request.data["text"]
            res = PlagCheck(text)
            return JsonResponse(res, safe=False)
        elif request.data["mode"] == "doc" and "file" in request.FILES.keys():
            text = request.FILES["file"].read().decode("utf-8")
            res = PlagCheck(text)
            return JsonResponse(res, safe=False)
        elif request.data["mode"] == "ocr" and "file" in request.FILES.keys():
            text = inference_web(request.FILES["file"])
            print(text)
            res = PlagCheck(text, n_grams=True)
            return JsonResponse(res, safe=False)
        else:
            return JsonResponse({"message": "Error has occured"})
