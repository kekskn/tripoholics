import React from "react";
import cn from "classnames";

import Avatar from "../Avatar/Avatar";
import MessageText from "./MessageText";

import "./MessageItem.scss";

export default function MessageItem({ isMy, isOnline, text, isRead }) {
  return (
    <div className={cn("message-item", { my: isMy })}>
      <div className="message-item__avatar">
        <Avatar height={40} width={40} isOnline={isOnline} />
      </div>
      <div className="message-item__info">
        <MessageText text={text} isRead={isRead} />
        <div className="message-item__date">12:37</div>
      </div>
    </div>
  );
}
