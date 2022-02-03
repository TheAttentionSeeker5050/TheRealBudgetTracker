function filter_by_type(entry_type) {
    // filters by entry type when you press the filter buttons "income" or "expense"
    let rows = document.querySelectorAll(".table_row");
    let type = entry_type;
    
    let income_filter_button = document.getElementById("income_filter_button")
    let expense_filter_button = document.getElementById("expense_filter_button")


    const remove_entry_type_filter = (element) => {
        // here we toogle the filter buttons
        for (var j = 0; j <element.length; j++) {
            element[j].classList.remove("is-hidden");
            console.log(element[j])
        }
    } 

    if (type === "All") {
        // here we deselect any entry type filters we previously had
        remove_entry_type_filter(rows)
        income_filter_button.classList.remove("is_selected")
        expense_filter_button.classList.remove("is_selected")

    } else {

        // we check if the button is already selected in order to toggle the filter

        if (type == "Income" && income_filter_button.classList.contains("is_selected")) {
            income_filter_button.classList.remove("is_selected")
            remove_entry_type_filter(rows)

        } else if (type == "Expense" && expense_filter_button.classList.contains("is_selected")) {
            expense_filter_button.classList.remove("is_selected")
            remove_entry_type_filter(rows)

        } else {

            // here we filter by type

            // but first we add the is_selected class. it does not do anything in css. it's just
            // for the toggle logic when a specific filter is selected twice
            if(type === "Income") {
                income_filter_button.classList.add("is_selected")
            } else if (type === "Expense") {
                expense_filter_button.classList.add("is_selected")
            }

            for (var i = 0; i <rows.length; i++){
                if (rows[i].classList.contains(type)) {
                    rows[i].classList.remove("is-hidden");
                } else {
                    rows[i].classList.add("is-hidden");
                }
            }

        }



        
    }
}