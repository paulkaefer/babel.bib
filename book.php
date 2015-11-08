<?php
    echo "Generating book.pdf, which will be loaded shortly. Thank you for your patience. If you need further assistance, ask a librarian. They may be found in every third hex."
    exec('python generateBook.py', $output);
    exec('pdflatex book.tex');
    exec('rm -rf /tmp/book/', $output);
    # redirect to book.pdf
?>