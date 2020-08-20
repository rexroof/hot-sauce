import os
from flask import Flask
app = Flask(__name__)

PEPPERS = int(os.getenv("PEPPERS", default=1000))

RATIO = PEPPERS / 1000

# 1510 peppers   1000
# 36 salt        24
# 124 sugar      82
# 45 garlic      30

# 266 vinegar    176

@app.route('/')
def hello_world():
    return f'''<p>
    Combine in a blender or a food processor (or finely chop) the following
    ingredients:</br>
    {PEPPERS}g any sort of hot or mild pepper </br>
    {24 * RATIO}g kosher salt </br>
    {82 * RATIO}g white sugar</br>
    {30 * RATIO}g fresh garlic</br>
    </br>
    Your mixure should be rather wet, add a little water if it isn't.  Put into mason
    jars or other glass containers.  Make sure you leave plenty of headroom.  This
    will grow as it ferments. Leave in relatively cool dark area for 10 days
    or up to two weeks.  Check on it every other day, look for bubbles. 
    </br>
    </br>
    After your mixture has fermented, add: </br>
    </br>

    {176 * RATIO}g white vinegar (or any good vinegar)</br>
    </br>
    And puree in blender until smooth.   Strain through your finest mesh strainer and
    simmer over low heat until you have a consistency you like.   It will thicken
    slightly as it cools.   Keep in a refridgerator, should last a year or two if
    kept cold.  Use your best judgement!

    </br>


    </p>'''

