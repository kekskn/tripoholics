import React from "react";
import { useDispatch, useSelector } from "react-redux";
import { RootState } from "src/redux/store";
import { Oval } from "react-loader-spinner";

import Avatar from "src/components/Chat/Avatar/Avatar";
import tripIcon from "../../../../../static/photos/Tripoholics-icon-white.png";
import fromIcon from "../../../../../static/photos/from.png";
import transportIcon from "../../../../../static/photos/transport.png";
import peopleIcon from "../../../../../static/photos/people.png";
import countriesIcon from "../../../../../static/photos/countries.png";
import citiesIcon from "../../../../../static/photos/cities.png";

export default function PopupUserInfo({ userId }) {
  const dispatch = useDispatch();

  const currentUser = useSelector((state: RootState) =>
    state.map.users.find((user) => user.id === userId)
  );
  const isLoadingNewDialog = useSelector(
    (state: RootState) => state.chat.isCreatingNewDialog
  );

  const handleWriteClick = () => {
    console.log("handleWriteClick");
    const data = { interlocutor_id: 9, author_id: 7 };
    // @ts-ignore
    dispatch(createNewDialog(data));
  };

  console.log("currentUser", currentUser);
  return (
    <>
      <div className="map__popup-left-block">
        <div className="map__popup-avatar">
          <Avatar width={90} height={90} isOnline={false} letter="Q" isSquare />
        </div>
        <div className="map__popup-descr">
          <div className="map__popup-descr-item descr-countries">
            <img src={countriesIcon} alt="" />
            <p className="map__popup-descr-countries-count">
              {currentUser?.countries_count}
            </p>
          </div>
          <div className="map__popup-descr-item descr-cities">
            <img src={citiesIcon} alt="" />
            <p className="map__popup-descr-cities-count">
              {currentUser?.cities_count}
            </p>
          </div>
        </div>
      </div>
      <div className="map__popup-right-block">
        <div className="map__popup-user">
          <div>
            <p className="map__popup-user-fio">{`${currentUser?.user_name} ${currentUser?.user_surname}`}</p>
            <p className="map__popup-user-nickname">
              {currentUser?.user_email}
            </p>
          </div>
          <div className="map__popup-icon">
            <img src={tripIcon} alt="" />
          </div>
        </div>
        <div className="map__popup-info">
          <div className="info-from info-icon">
            <img src={fromIcon} alt="" />
            <p className="info-from__text">{currentUser?.from}</p>
          </div>
          <div className="info-transport info-icon">
            <img src={transportIcon} alt="" />
            <p className="info-from__text">{currentUser?.transport}</p>
          </div>
          <div className="info-people info-icon">
            <img src={peopleIcon} alt="" />
            <p className="info-from__text">{currentUser?.people}</p>
          </div>
        </div>
        <div className="map__popup-btns">
          <button
            className="map__popup-btn profile-btn"
            onClick={() => {
              console.log("CLICKED!");
              // dispatch(fetchUserPopupInfo(userId));
              // getUserPopupInfo(12);
            }}
          >
            Профиль
          </button>
          <button
            className="map__popup-btn message-btn"
            onClick={handleWriteClick}
          >
            {isLoadingNewDialog ? (
              <Oval
                height={20}
                width={20}
                color="#4fa94d"
                wrapperStyle={{}}
                wrapperClass=""
                visible={true}
                ariaLabel="oval-loading"
                secondaryColor="#4fa94d"
                strokeWidth={2}
                strokeWidthSecondary={2}
              />
            ) : (
              "Написать"
            )}
          </button>
        </div>
      </div>
    </>
  );
}
