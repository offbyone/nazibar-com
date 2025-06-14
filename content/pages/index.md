---
title: Nazi Bar List
save_as: index.html
template: page
---

<details open>
<summary>
What is a Nazi Bar?
</summary>
<p>A "Nazi bar" is a reference to the saying: "If there's a Nazi at the table and 10 other people sitting there talking to him, you got a table with 11 Nazis." This site tracks vendors and platforms that allow Nazi and fascist content to proliferate.</p>
</details>

## The List

<table class="sortable">
<thead>
<tr><th>Vendor</th><th>Why?</th><th>Date Updated</th></tr>
</thead>
<tbody>
{% for vendor in vendors %}
<tr>
<td markdown="span"><a href="{{ vendor.url }}">{{ vendor.name }}</a></td>
<td>{{ vendor.reason }}</td>
<td>{{ vendor.updated_at|default('') }}</td>
</tr>
{% endfor %}
</tbody>
</table>

## FAQs

<details>
<summary>
Why are you tracking these vendors?
</summary>
<p>By highlighting vendors that tolerate Nazi and fascist content, we aim to inform consumers and encourage these platforms to take a stronger stance against hate.</p>
</details>
