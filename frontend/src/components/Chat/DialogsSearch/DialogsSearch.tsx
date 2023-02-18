import React from "react";

import "./DialogsSearch.scss";

export default function DialogsSearch() {
  return (
    <div className="chat__dialogs-search">
      <div className="chat__dialogs-search-input-wrapper">
        <input className="chat__dialogs-search-input" placeholder="Поиск" />
      </div>
    </div>
  );
}
