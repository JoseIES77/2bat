---
titlepage: false
lang: es
toc: false
footer-right: \thepage/\pageref{LastPage}
header-includes:
  - \usepackage{graphicx}
  - \usepackage{lastpage}
  - \usepackage{xltxtra}
  - \usepackage{listings}
  - \usepackage{pdflscape}
  - \usepackage{awesomebox}
  - \usepackage{xcolor,tikz,tcolorbox}
  - \usepackage{caption}
  - \usepackage{emoji}
  - \usepackage{eso-pic}
  - \AddToShipoutPictureBG{
      \ifthenelse{\value{page}=1}{
        \includegraphics[width=\paperwidth,height=\paperheight]{img/portadaEx.png}
      }{
        \includegraphics[width=\paperwidth,height=\paperheight]{img/paginasEx.png}
      }
    }
  - \setemojifont{Noto Color Emoji}
  - \tcbuselibrary{raster}
  - \definecolor{lightblue}{rgb}{0.68, 0.85, 0.9}
  - \definecolor{ballblue}{rgb}{0.13, 0.67, 0.8}
  - \definecolor{cerulean}{rgb}{0.0, 0.48, 0.65}
  - \definecolor{almond}{rgb}{0.94, 0.87, 0.8}
  - \definecolor{apricot}{rgb}{0.98, 0.81, 0.69}
  - \definecolor{cream}{rgb}{1.0, 0.99, 0.82}
  - \definecolor{coralred}{rgb}{1.0, 0.25, 0.25}
  - \definecolor{byzantium}{rgb}{0.44, 0.16, 0.39}
  - \definecolor{thistle}{rgb}{0.85, 0.75, 0.85}
  - \definecolor{ceruleanblue}{rgb}{0.16, 0.32, 0.75}
  - \definecolor{beaublue}{rgb}{0.74, 0.83, 0.9}
  - \renewcommand{\normalsize}{\small}
...

\begin{table}[h!]
\centering
\begin{tabular}{|p{1.2cm}|p{1.2cm}|p{1.2cm}|p{1.2cm}|p{1.2cm}|p{1.2cm}|p{1.2cm}|p{1.2cm}|p{1.2cm}|p{1.2cm}|}
\hline
1 & 2 & 3 & 4 & 5 & 6 & 7 & 8 & 9 & 10 \\
\hline
d & d & d & b & d & b & c & c & d & c \\
\hline
\end{tabular}
\end{table}

\begin{table}[h!]
\centering
\begin{tabular}{|p{1.2cm}|p{1.2cm}|p{1.2cm}|p{1.2cm}|p{1.2cm}|p{1.2cm}|p{1.2cm}|p{1.2cm}|p{1.2cm}|p{1.2cm}|}
\hline
11 & 12 & 13 & 14 & 15 & 16 & 17 & 18 & 19 & 20 \\
\hline
c & b & c & b & a & d & c & c & d & b \\
\hline
\end{tabular}
\end{table}

\begin{table}[h!]
\centering
\begin{tabular}{|p{1.2cm}|p{1.2cm}|p{1.2cm}|p{1.2cm}|p{1.2cm}|p{1.2cm}|p{1.2cm}|p{1.2cm}|p{1.2cm}|p{1.2cm}|}
\hline
21 & 22 & 23 & 24 & 25 & 26 & 27 & 28 & 29 & 30 \\
\hline
b & b & c & b & c & d & c & a & b & a \\
\hline
\end{tabular}
\end{table}
