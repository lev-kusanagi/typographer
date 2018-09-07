import os
import argparse

textList = ['\\documentclass[svgnames]{article}\n', '\\usepackage{calligra,xcolor,wallpaper}\n', '% \\usepackage[driver=pdflatex]{hand}\n', '% \\usepackage[T1]{fontenc}\n', '\\usepackage[spanish]{babel}\n', '\n', '\\definecolor{red}{HTML}{BC0000}% blue 0D1126\n', '\n', '\\renewcommand{\\text}{llare, senora mia -dijo don Quijote-; y los que hare el tiempo embendarse en esta tenganza que al primer piedra caida tienen de manera que la discurso de Lotario la caballeris y satisfacion sobresaltase, que tu por la andasente desde alli fui nuestra seguro, no no vetar de suyos; y asi, infinito es el que en tierra templa, Sancho, santandoles los saren ni tendre arbuyas hayas y asentado.  -Yo te son, que plesra borrica se le enabinaba Sancho que daba por el legua de la consejo, no era partes por soltar, por bolso della, y tanto que este como daban las espadas de la caza.  -Por su verdad -respondio el de la Montesinos.}\n', '\n', '\n', '\n', '\\title{del Escritorio de Miguel de Cervantes de Saavedra}\n', '\\author{}\n', '\\begin{document}\\pagestyle{empty}\\CenterWallPaper{}{parchemin_1.jpg}\n', '  \\calligra\\Large\n', '  {\\color{black}\\maketitle}\n', '  \\begin{handpar}\n', '    \\text\n', '  \\end{handpar}\n', '  \\color{MidnightBlue}\n', '\\end{document}\n']

parser = argparse.ArgumentParser()
parser.add_argument('input_words', metavar='N', type=str, nargs='+')
input = parser.parse_args()
myText = ' '.join(input.input_words)

textList[8] = '\\renewcommand{\\text}{' + myText + '}\n'

with open('typographed_cervantes.tex', 'w') as fout:
    for i in range(len(textList)):
        fout.write(textList[i])

os.system("pdflatex -interaction=nonstopmode typographed_cervantes.tex")
os.system("mv typographed_cervantes.pdf iexec/")
