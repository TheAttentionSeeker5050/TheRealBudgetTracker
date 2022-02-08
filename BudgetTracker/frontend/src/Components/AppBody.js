import React,  { useState } from "react";

import {EntriesLog, EntryItem} from './EntriesLog';

// the api rest framework
import axios from "axios";



// const entry_list = []


function AppBody() {

  let [entryList, setEntryList] = useState([])

  // we get or refresh list
  const refreshList = () => {
    axios
      .get("/api/entries/")
      .then((res) => { 
        setEntryList(res.data)
      })
      .catch((err) => console.log(err));
  };

  return (
    <div className="app_body">
      <EntriesLog>

        {refreshList()}
        {console.log(entryList)}
        {console.log(typeof(entryList))}
        {entryList.map(
          (entry) => (
            <EntryItem
              entry_type={entry.entry_type}
              description={entry.description}
              category={entry.category}
              date={entry.date}
              amount={entry.amount}
            />
          )
        )}

      </EntriesLog>
    </div>
  );

}

export {AppBody};