# Makefile

.PHONY: setup preprocess train evaluate predict all

setup:
	pip install -r requirements.txt

preprocess:
	python src/preprocess.py

train:
	python src/train.py

evaluate:
	python src/evaluate.py

predict:
	python src/predict.py

all: preprocess train evaluate predict

make setup
make preprocess
make train
make evaluate
make predict