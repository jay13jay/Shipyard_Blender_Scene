# {{ title }}

## Description
___
{{ desc }}


### Asset Gallery
___
|Title| Image | Description|
--- | --- | ---
{% for n in names %}
|{{ n[1] }}| ![{{ n[1] }}]({{ n[0] }}) | |
{% endfor %}


=(INDEX(Banana!$A:$A,MATCH($A6,Banana!$A:$A,0)))