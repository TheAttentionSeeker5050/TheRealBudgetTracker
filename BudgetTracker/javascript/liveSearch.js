function liveSearch() {
    // Locate the row elements
    let rows = document.querySelectorAll('.table_row')
    // Locate the search input
    let search_query = document.getElementById("searchbox").value;
    // Loop through the cards
    for (var i = 0; i < rows.length; i++) {
      // If the text is within the card...
      if(rows[i].innerText.toLowerCase()
        // ...and the text matches the search query...
        .includes(search_query.toLowerCase())) {
          // ...remove the `.is-hidden` class.
          rows[i].classList.remove("is-hidden");
      } else {
        // Otherwise, add the class.
        rows[i].classList.add("is-hidden");
      }
    }
  }