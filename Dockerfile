FROM ubuntu:16.04
COPY * /
RUN apt-get update && apt-get install -y texlive-latex-base texlive-fonts-recommended
