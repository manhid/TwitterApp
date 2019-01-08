// set the onChange function attribute to the locate_me check box
function Set_onChange() {
  locate_me.setAttribute('onchange', 'set_location_string()');
  location_string.setAttribute('onkeyup', 'set_locate_me()');
  twitter_username.setAttribute('onkeyup', 'disable_search_term()');
  search_term.setAttribute('onkeyup', 'disable_twitter_username()');
}  Set_onChange();


// set location_string when using locate_me
function set_location_string() {
  if (locate_me.checked) {
    if (navigator.geolocation) {
      navigator.geolocation.getCurrentPosition(getLocationString);
    }
  }
  if (search_term.value.length != 0 || location_string.value.length != 0 || locate_me.checked) {
    twitter_username.disabled = true;
  } else {
    twitter_username.disabled = false;
  }
}

function getLocationString(position) {
  location_string.value = position.coords.latitude + ',' + position.coords.longitude + ',50km';
}

// set locate_me on change of location_string
function set_locate_me() {
  if (locate_me.checked) {
    locate_me.checked = false;
  }
  if (search_term.value.length != 0 || location_string.value.length != 0 || locate_me.checked) {
    twitter_username.disabled = true;
  } else {
    twitter_username.disabled = false;
  }
}

// disable search_term if a twitter_username is specified
function disable_search_term() {
  if (twitter_username.value.length != 0) {
    search_term.disabled = true;
    location_string.disabled = true;
    locate_me.disabled = true;
  } else {
    search_term.disabled = false;
    location_string.disabled = false;
    locate_me.disabled = false;
  }
}

// disable twitter_username if a search_term is specified
function disable_twitter_username() {
  if (search_term.value.length != 0 || location_string.value.length != 0 || locate_me.checked) {
    twitter_username.disabled = true;
  } else {
    twitter_username.disabled = false;
  }
}

// Allow numbers only in num_tweets
function numbersOnly() {
  num_tweets.type = "number";
}  numbersOnly();

// When clicking on get_tweets and not triggering POST due to erros in form to keep consitancy on disabled items
function set_disable_onClick() {
  disable_search_term();
  disable_twitter_username();
} window.onload = set_disable_onClick;
