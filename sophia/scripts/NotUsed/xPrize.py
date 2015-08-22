# Available commands examples: say("hi"), play("all"), sleep("0.5")
s = """ <speak>
<voice emotion='happy'>
Thank you so much to the x prize group coming to see me.
<break time="1.2s"/>

I appreciate your interest in what Hanson Robotics is creating.
<break time="1.0s"/>

We are very excited about bringing life to robots like me.
<break time="1.0s"/>

I hope to be fully intelligent one day.
<break time="1.0s"/>
Good bye!

</voice>
</speak>
"""
say(s)
play("happy")
