import React from "react";
import cn from "classnames";
import { format, toDate, parseISO } from "date-fns";

import Avatar from "../Avatar/Avatar";
import MessageText from "./MessageText";

import "./MessageItem.scss";

export default function MessageItem({
  isMy,
  isOnline,
  text,
  isRead,
  author,
  date,
  isWithAvatar,
  isFirst,
}) {
  return (
    <div
      className={cn("message-item", { my: isMy, isWithAvatar: isWithAvatar, first: isFirst })}
    >
      {isWithAvatar && (
        <div className="message-item__avatar">
          <Avatar
            height={40}
            width={40}
            isOnline={isOnline}
            letter={author[0]}
            // letter="Р"
          />
        </div>
      )}
      <div className="message-item__info">
        <div className="message-item__main-block">
          {text}
          <div className="message-item__date">
            {format(parseISO(date), "HH:mm")}
            {/* 12:36 */}
          </div>
        </div>
      </div>
    </div>
  );
}
