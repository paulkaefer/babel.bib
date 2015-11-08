<?php
    exec('python generateBook.py', $output);
    exec('pdflatex book.tex');
    exec('rm -rf /tmp/book/', $output);
    # redirect to book.pdf
?>