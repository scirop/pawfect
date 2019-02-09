/**
 * A handler function to prevent default submission and run our custom script.
 * @param  {Event} event  the submit event triggered by the user
 * @return {void}
 */
 function generateJson() = event => {
  
  // Stop the form from submitting since we’re handling that with AJAX.
  event.preventDefault();
  
  // TODO: Call our function to get the form data.
  const data = {};
  
  // Demo only: print the form data onscreen as a formatted JSON object.
  const dataform = document.getElementsByClassName('specification-form');
  
  // Use `JSON.stringify()` to make the output valid, human-readable JSON.
  dataform.textContent = JSON.stringify(data, null, "  ");
  
  // ...this is where we’d actually do something with the form data...
};