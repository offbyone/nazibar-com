---
title: Nazi Bar List
save_as: index.html
template: page
---

<details closed>
<summary>
What is a Nazi Bar?
</summary>
<p>A "Nazi bar" is a reference to a classic Twitter thread. This site tracks vendors and platforms that allow Nazi and fascist content to proliferate.</p>

<blockquote class="twitter-tweet" data-width="550" data-dnt="true">

<p>I was at a shitty crustpunk bar once getting an after-work beer. One of those shitholes where the bartenders clearly hate you. So the bartender and I were ignoring one another when someone sits next to me and he immediately says, "no. get out."</p>

<p>And the dude next to me says, "hey i'm not doing anything, i'm a paying customer." and the bartender reaches under the counter for a bat or something and says, "out. now." and the dude leaves, kind of yelling. And he was dressed in a punk uniform, I noticed</p>

<p>Anyway, I asked what that was about and the bartender was like, "you didn't see his vest but it was all nazi shit. Iron crosses and stuff. You get to recognize them."
</p>

<p>And i was like, ohok and he continues.
</p>

<p>"you have to nip it in the bud immediately. These guys come in and it's always a nice, polite one. And you serve them because you don't want to cause a scene. And then they become a regular and after awhile they bring a friend. And that dude is cool too.
</p>

<p>And then THEY bring friends and the friends bring friends and they stop being cool and then you realize, oh shit, this is a Nazi bar now. And it's too late because they're entrenched and if you try to kick them out, they cause a PROBLEM. So you have to shut them down.
</p>

<p>And i was like, 'oh damn.' and he said "yeah, you have to ignore their reasonable arguments because their end goal is to be terrible, awful people."
</p>
<p>And then he went back to ignoring me. But I haven't forgotten that at all.</p>
— Michael Tager (@IamRageSparkle) <a href="https://web.archive.org/web/20221221103518/https://twitter.com/IamRageSparkle/status/1280891537451343873?ref_src=twsrc%5Etfw">July 8, 2020</a></blockquote>
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
