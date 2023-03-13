import React from "react";

import "./EmptyChat.scss";
import emptyChat from "../../../../../static/photos/icons/empty-chat.png";
import noMessages from "../../../../../static/photos/icons/empty-folder.png";

export default function EmptyChat({ isNewDialog }) {
  return (
    <div
      className="empty-chat"
      style={isNewDialog ? { marginTop: "250px" } : {}}
    >
      <div className="empty-chat__icon">
        <img
          src={isNewDialog ? noMessages : emptyChat}
          alt=""
          className="empty-chat__icon-img"
        />
      </div>
      <div className="empty-chat__descr">
        {isNewDialog
          ? "Диалог пуст.\nНапишите первое сообщение"
          : "Выберите диалог из списка"}
      </div>
    </div>
  );
}
