document.addEventListener('keypress', function(event) {
  if (event.key === 'Enter' && (document.activeElement.tagName.toLowerCase() !== 'button')) {
  
    let javascriptData = document.getElementById('textInput').value
    fetch('http://127.0.0.1:5000/postmethod',  {
      method: 'POST',
      body: JSON.stringify(javascriptData),
      headers: new Headers({
        'Content-Type': 'application/json'
      })
    })
    fetch('http://127.0.0.1:5000/getpythondata')
      .then(res => res.json())
      .then(data => { 
    
        const para = document.createElement('P');
        const t = document.createTextNode(`You: ${javascriptData}`);
        para.appendChild(t);
        document.getElementById('box').appendChild(para);
            
        const para2 = document.createElement('p');
        para2.className = "bot";
        const tb = document.createTextNode(data);
        
        para2.appendChild(tb);
        document.getElementById('box').appendChild(para2);

        const userInput = document.getElementById('textInput').value.toLowerCase();

        if(userInput.startsWith('google')) { //make it downcase when checking!
          window.open(`https://www.google.com/search?q=${userInput.replace('google', '')}`, '_blank')
        };
        
        document.getElementById('textInput').value = ''
        window.scrollTo(0,document.body.scrollHeight);
    
    });
   }
  });
  