ID: {{it.id}}<br>
Имя: {{it.fullName}}<br>
Должность: {{it.position}}<br>
Дата создания записи: {{it.creationTime}}<br>
<a href="/showform/{{it.id}}">Изменить</a>
<a href="/delete/{{it.id}}">Удалить</a><br>
{%if it.position != "Инженер" %}
Подчиненные: <br>
    {% for it in it.childs %}
	
	{% include "item.tpl" ignore missing %}  

    {% endfor %}
{%endif%}

<br><br>
