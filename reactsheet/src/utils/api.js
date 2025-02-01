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
