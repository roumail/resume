# Resume release 1

## Overview

First version of the resume builder. It allows one to use to the
`generate-resume` entrypoint to create and index.html that `jekyll` can render
and `wkhtmltopdf` can use to create a pdf version from.

The separation of concern is done to separate the templating/styling of the cv
from the cv data which is constantly changing
