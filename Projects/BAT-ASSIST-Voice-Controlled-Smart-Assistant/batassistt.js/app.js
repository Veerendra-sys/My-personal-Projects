const btn = document.querySelector(".talk");
const content = document.querySelector(".content");
const darkModeBtn = document.querySelector('.dark-mode-btn');
const undoBtn = document.querySelector('.undo-btn');
const body = document.querySelector('body');

// Function to speak text
function speak(text) {
  const text_speak = new SpeechSynthesisUtterance(text);
  text_speak.rate = 1;
  text_speak.volume = 1;
  text_speak.pitch = 1;
  window.speechSynthesis.speak(text_speak);
}

// Function to wish the user based on time
function wishMe() {
  const day = new Date();
  const hour = day.getHours();

  if (hour >= 0 && hour < 12) {
    speak("morning sir...");
  } else if (hour >= 12 && hour < 17) {
    speak("afternoon sir...");
  } else {
    speak("evening sir...");
  }
}

// Initialize and greet the user
window.addEventListener("load", () => {
  speak("BAT ASSIST IS ACTIVE...");
  wishMe();
});

// Set up speech recognition
const SpeechRecognition = window.SpeechRecognition || window.webkitSpeechRecognition;
const recognition = new SpeechRecognition();


recognition.onresult = (event) => {
  // Only process final results
  if (!event.results[event.resultIndex].isFinal) return;

  const currentIndex = event.resultIndex;
  const transcript = event.results[currentIndex][0].transcript;
  content.textContent = transcript;
  takeCommand(transcript.toLowerCase());
};


btn.addEventListener("click", () => {
  content.textContent = "Listening....";
  recognition.start();
});

// Function to verify Batcave access


  
// Function to handle commands
function takeCommand(message) {
  if (message.includes("i'm batman") || message.includes("i am batman")) {
    speak("I know, Master Wayne.");
  } else if (message.includes("alfred report")) {
    speak("All systems online. City’s calm, for now.");
  } else if (message.includes("where is the batmobile") || message.includes("where's the batmobile")) {
    speak("Batmobile is in stealth mode, parked a block away.");
  } else if (message.includes("activate stealth mode")) {
    darkModeBtn.click();
    speak("Stealth mode activated.");
    
    const stealthSound = new Audio("stealth.mp3");
    stealthSound.play();
    
  } else if (message.includes("turn on dark mode") || message.includes("this is serious")) {
    darkModeBtn.click();
  } else if (message.includes("undo dark mode")) {
    undoBtn.click();
  } else if (message.includes("open cave")) {
  speak("Opening the Batcave.");
  window.location.href = "batcave.html";  // Correctly opens the Batcave page
} else if (message.includes("open creative")) {
  speak("welcome to our creatives.");
  window.location.href = "creative.html"; // opens creatives 

  } else if (message.includes("hey") || message.includes("hello")) {
    speak("Hello Sir, still saving the city?");
  } else if (message.includes("how are you") || message.includes("your status")) {
    speak("Better than ever, sir.");
  } else if (message.includes("open google")) {
    window.open("https://google.com", "_blank");
    speak("Opening Google...");
  } else if (message.includes("open youtube")) {
    window.open("https://youtube.com", "_blank");
    speak("Opening YouTube...");
  } else if (message.includes("open facebook")) {
    window.open("https://facebook.com", "_blank");
    speak("Opening Facebook...");
  } else if (message.includes("search on youtube")) {
    const query = message.replace("search on youtube", "").trim();
    const url = `https://www.youtube.com/results?search_query=${encodeURIComponent(query)}`;
    window.open(url, "_blank");
    speak(`Searching ${query} on YouTube.`);
  } else if (message.includes("search on instagram")) {
    const query = message.replace("search on instagram", "").trim();
    const url = `https://www.instagram.com/explore/tags/${encodeURIComponent(query)}/`;
    window.open(url, "_blank");
    speak(`Searching ${query} on Instagram.`);
  } else if (message.includes("search on google")) {
    const query = message.replace("search on google", "").trim();
    const url = `https://www.google.com/search?q=${encodeURIComponent(query)}`;
    window.open(url, "_blank");
    speak(`Searching ${query} on Google.`);
  } else if (message.includes("play")) {
    const song = message.replace("play", "").replace("on spotify", "").trim();
    const url = `https://open.spotify.com/search/${encodeURIComponent(song)}`;
    window.open(url, "_blank");
    speak(`Playing ${song} on Spotify.`);
  } else if (
    message.includes("google for me") ||
    message.includes("who is") ||
    message.includes("what are") ||
    message.includes("crime rate")
  ) {
    const searchUrl = `https://www.google.com/search?q=${encodeURIComponent(message)}`;
    window.open(searchUrl, "_blank");
    speak(`This is what I found on the internet regarding ${message}.`);
  } else if (message.includes(" scearch on wikipedia")) {
    const searchUrl = `https://en.wikipedia.org/wiki/${message.replace("wikipedia", "").trim()}`;
    window.open(searchUrl, "_blank");
    speak(`This is what I found on Wikipedia regarding ${message}.`);
  } else if (message.includes("time right now")) {
    const time = new Date().toLocaleString(undefined, {
      hour: "numeric",
      minute: "numeric",
      hour12: true,
    });
    speak(`The current time is ${time}.`);
  } else if (message.includes("date")) {
    const date = new Date().toLocaleString(undefined, {
      month: "long",
      day: "numeric",
      year: "numeric",
    });
    speak(`Today's date is ${date}.`);
  } else if (message.includes("calculator")) {
    speak("Sorry, I can't open the calculator directly.");
  } else if (message.includes("i am no hero")) {
    speak("You either die a hero or live long enough to see yourself become the villain.");
  } else if (message.includes("yes i am")) {
    speak("Old habits don't wear off, Master. I'm here for you.");
  } else {
    const searchUrl = `https://www.google.com/search?q=${encodeURIComponent(message)}`;
    window.open(searchUrl, "_blank");
    speak(`I found some information for ${message}`);
  }
}


// Function to toggle dark mode
function toggleDarkMode() {
  body.style.backgroundColor = 'black';
  body.style.color = 'white';
  darkModeBtn.style.display = 'none';
  undoBtn.style.display = 'block';
  speak("Dark mode is now enabled.");
}

// Function to revert to light mode
function undoDarkMode() {
  body.style.backgroundColor = 'white';
  body.style.color = 'black';
  darkModeBtn.style.display = 'block';
  undoBtn.style.display = 'none';
  speak("Dark mode has been disabled.");
}

// Event listeners for button clicks
darkModeBtn.addEventListener('click', toggleDarkMode);
undoBtn.addEventListener('click', undoDarkMode);
