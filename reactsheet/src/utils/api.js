export function makeRequest(url) {
  const data = fetch(url)
    .then(response => {
      if (response.ok) {
        return response.json();
      } else {
        throw new Error("API request failed");
      }
    })
    .then(data => {
      return JSON.parse(data);
    })
    .catch(error => {
      console.error(error);
    });
  return data;
}

async function foo(url) {}

async function bar(url) {
  fetch(url)
    .then(response => {
      if (response.ok) {
        return response.json(); // Parse the response data as JSON
      } else {
        throw new Error("API request failed");
      }
    })
    .then(data => {
      // Process the response data here
      console.log(data); // Example: Logging the data to the console
    })
    .catch(error => {
      // Handle any errors here
      console.error(error); // Example: Logging the error to the console
    });
}
