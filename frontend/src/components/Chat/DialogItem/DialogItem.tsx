import React from "react";
import { formatDistance, subDays } from "date-fns";
import ru from "date-fns/esm/locale/ru/index.js";

import Avatar from "../Avatar/Avatar";
import maxMessageLengthCalc from "../../../utils/maxMessageLengthCalc";
// import maxMessageLengthCalc from "src/utils/maxMessageLengthCalc";

import "./DialogItem.scss";

export default function DialogItem({ date }) {
  //   const date = new Date(2022, 10, 5);
  //   const date = new Date(Date.now() - 100000);
  return (
    <div className="dialog-item">
      <div className="dialog-item__avatar">
        <Avatar height={48} width={48} isOnline />
      </div>
      <div className="dialog-item__info-wrapper">
        <div className="dialog-item__info">
          <div className="dialog-item__fullname">Тест Тестов</div>
          <div className="dialog-item__date">
            {formatDistance(date, new Date(), { addSuffix: true, locale: ru })}
          </div>
        </div>
        <div className="dialog-item__messages">
          <div className="dialog-item__last-message">
            {maxMessageLengthCalc("Приветик, как дела? Я тут вспомнил...")}
          </div>
          <div className="dialog-item__unread-messages">3</div>
        </div>
      </div>
    </div>
  );
}
