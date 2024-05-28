/**
  Fetches a message from the server and displays it in the result div.
  URL corrected to match the port where FastAPI server runs.
 */
async function callMessage() {
    try {
        const response = await fetch('http://localhost:8000/hello_ud');
        const data = await response.text();
        document.getElementById('result').textContent = data;
    } catch (error) {
        console.error('Error:', error);
    }
}

/**
here was an error with the archive index.html because it was calling a class named "calltable"
and in the javascript was called as "callWebServices" so the index didnt found tghe class

i already make the correction in the javascrip
 */
async function callTable() {
    try {
        const response = await fetch('http://localhost:8000/products');
        const data = await response.json();
        
        let table = '<table>';
        table += '<tr><th>ID</th><th>Name</th><th>Description</th></tr>';
        
        data.forEach(item => {
            table += `<tr><td>${item.id}</td><td>${item.name}</td><td>${item.description}</td></tr>`;
        });
        
        table += '</table>';
        
        document.getElementById('result').innerHTML = table;
    } catch (error) {
        console.error('Error:', error);
    }
}
