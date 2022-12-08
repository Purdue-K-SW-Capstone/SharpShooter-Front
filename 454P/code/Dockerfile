ARG BASE_CONTAINER=jupyter/minimal-notebook
FROM $BASE_CONTAINER
LABEL author = "Seokhyeon Bang"

USER root

RUN pip install pandas numpy matplotlib

USER $NB_UID
