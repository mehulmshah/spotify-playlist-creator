## The Idea

I started this project after browsing the [Spotify Web API](https://beta.developer.spotify.com/documentation/web-api). It's very thorough and well documented, I highly recommend taking a look when you have some free time. I noticed the ability to generate song listings based on a combination of seed artists/genres/songs and certain characteristics outlined in the [recommendation](https://beta.developer.spotify.com/documentation/web-api/reference/browse/get-recommendations) documentation. So I envisioned a webapp where one could generate a personalized playlist for any occasion with a simple, intuitive UI. 

## The Code

Luckily for me, someone created a python wrapper for the API, called [spotipy](https://github.com/plamere/spotipy). This made interacting with the API much simpler. I opt

## The UI

With this web app, I wanted simplicity to be the highest priority. With multiple characteristic options that don't have the most obvious names (I haven't heard the word _valence_ since high school chemistry), I had to devise a way to let users understand the playlist weights in an unobtrusive way. I ended up going with small help bubbles that pop up when a user hovers their mouse over the information bubble next to each feature.

Next, and perhaps most importantly, how do users select their ratios (on a scale of 0.0 - 1.0 for the most part)? Text boxes? Drop-down lists? Speaking their value of choice into a microphone? In the end, I ended up going with a slider bar. It felt like the easiest way for someone to choose a discrete value from 0 to 1, without having to type, click, or scroll. 
### Support or Contact

Having trouble with Pages? Check out our [documentation](https://help.github.com/categories/github-pages-basics/) or [contact support](https://github.com/contact) and we’ll help you sort it out.
