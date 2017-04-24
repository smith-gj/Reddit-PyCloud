# Code based off masked example from https://amueller.github.io/word_cloud
from os import path
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator

d = path.dirname(__file__)

# Read the whole text.
text = open(path.join(d, 'results.txt')).read()

# read and color the mask image
# http://reddits-world.wikia.com/wiki/Snoo
reddit_coloring = np.array(Image.open(path.join(d, "snoo.png")))

wc = WordCloud(background_color="white", max_words=2000, mask=reddit_coloring,
                max_font_size=40, random_state=42)

# generate word cloud
wc.generate(text)

# create coloring from image
image_colors = ImageColorGenerator(reddit_coloring)

# show
plt.imshow(wc, interpolation="bilinear")
plt.axis("off")
plt.figure()
# recolor wordcloud and show
# we could also give color_func=image_colors directly in the constructor
plt.imshow(wc.recolor(color_func=image_colors), interpolation="bilinear")
plt.axis("off")
plt.figure()
plt.imshow(reddit_coloring, cmap=plt.cm.gray, interpolation="bilinear")
plt.axis("off")
plt.show()
