

This is the fade-in-out module.

Simply include the following three lines in your html <head> to set it up:

<link rel="stylesheet" href="resources/fade-in-out/fade-in-out.css" type="text/css">
<script src="resources/fade-in-out/jquery-3.6.0.min.js"></script>
<script src="resources/fade-in-out/fade-in-out.js"></script>

Then give any div one of either class:
- <div class="fade-in"> to fade in and out left-to-right
- <div class="fade-in-diag"> to fade in and out diagonally at a 31deg angle

The fade-in animations will automatically play when the page loads
The fade-out animations will automatically play when a link is clicked that leads to a page with the same domain.

To set durations/angles:

For fade-in animations its sufficient to edit the values in fade-in-out.css
For fade-out animations you have to change the value in fade-in-out.js aswell (in delay(...))
