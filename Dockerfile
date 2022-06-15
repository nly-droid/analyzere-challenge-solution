FROM python

LABEL author="Nhi Ly"

ADD compute.py .

ENTRYPOINT ["python", "./compute.py"]
