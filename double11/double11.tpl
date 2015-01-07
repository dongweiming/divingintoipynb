{%- extends 'basic.tpl' -%}
{% from 'mathjax.tpl' import mathjax %}


{%- block header -%}
<!DOCTYPE html>
<html>
<head>

<meta charset="utf-8" />
<title>{{resources['metadata']['name']}}</title>

<script src="http://apps.bdimg.com/libs/require.js/2.1.11/require.min.js"></script>
<script src="http://apps.bdimg.com/libs/jquery/2.1.1/jquery.min.js"></script>

{% for css in resources.inlining.css -%}
<style type="text/css">
{{ css }}
</style>
{% endfor %}

<style type="text/css">
/* Overrides of notebook CSS for static HTML export */
body {
overflow: visible;
padding: 8px;
}

div#notebook {
overflow: visible;
border-top: none;
}

@media print {
div.cell {
display: block;
page-break-inside: avoid;
}
div.output_wrapper {
display: block;
page-break-inside: avoid;
}
div.output {
display: block;
page-break-inside: avoid;
}
}
</style>

<!-- Custom stylesheet, it must be in the same directory as the html file -->
<link rel="stylesheet" href="static/css/ipynb.css">

</head>
{%- endblock header -%}

{% block body %}
<body>
<div class="navbar navbar-static-top border-box-sizing" id="header">
<div class="container">
<div class="nav brand pull-left" id="ipython_notebook">
<a alt="dashboard" href="http://dongxi.douban.com/1111">
<img alt="IPython Notebook" src="static/images/dongxi.jpg">
</a>
</div>
</div>
</div>
<div tabindex="-1" id="notebook" class="border-box-sizing">
<div class="container" id="notebook-container">
{{ super() }}
</div>
</div>
</body>
{%- endblock body %}

{% block footer %}
</html>
{% endblock footer %}
