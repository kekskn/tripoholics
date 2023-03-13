// import { useState, useEffect } from "react";

// export const usePosition = () => {
//   const [position, setPosition] = useState({});
//   const [error, setError] = useState(null);

//   const onChange = (position: GeolocationPosition) => {
//     // Здесь мы могли бы сохранить весь объект position, но для
//     // ясности давайте явно перечислим, какие свойства нас интересуют.
//     setPosition({
//       latitude: position.coords.latitude,
//       longitude: position.coords.longitude,
//     });
//   };

//   const onError = (error) => {
//     setError(error.message);
//   };

//   useEffect(() => {
//     const geo = navigator.geolocation;

//     geo.getCurrentPosition((position) => {
//       // гарантированно получили объект с геопозицией
//       const {
//         coords: { latitude, longitude },
//       } = position;
//       // выводим результат в консоль
//       console.log("Coords after getCurrentPosition:", latitude, longitude);
//       // сохраним координаты в стейт
//       setPosition({ latitude, longitude });
//       console.log("position inside hook", position);
//     });
//     console.log("inside hook");

//     if (!geo) {
//       setError("Геолокация не поддерживается браузером");
//       return;
//     }

//     // Подписываемся на изменение геопозиции браузера.
//     const watcher = geo.watchPosition(onChange, onError);

//     // В случае, если компонент будет удаляться с экрана
//     // производим отписку от слежки, чтобы не засорять память.
//     return () => geo.clearWatch(watcher);
//   }, []);

//   return { ...position, error };
// };

import { useState, useEffect } from "react";

const defaultSettings = {
  enableHighAccuracy: false,
  timeout: Infinity,
  maximumAge: 0,
};

export const usePosition = (watch = false, userSettings = {}) => {
  const settings = {
    ...defaultSettings,
    ...userSettings,
  };

  const [position, setPosition] = useState({});
  const [error, setError] = useState(null);

  const onChange = ({ coords, timestamp }) => {
    setPosition({
      latitude: coords.latitude,
      longitude: coords.longitude,
      accuracy: coords.accuracy,
      speed: coords.speed,
      heading: coords.heading,
      timestamp,
    });
  };

  const onError = (error) => {
    setError(error.message);
  };

  useEffect(() => {
    if (!navigator || !navigator.geolocation) {
      setError("Geolocation is not supported");
      return;
    }

    if (watch) {
      const watcher = navigator.geolocation.watchPosition(
        onChange,
        onError,
        settings
      );
      return () => navigator.geolocation.clearWatch(watcher);
    }

    navigator.geolocation.getCurrentPosition(onChange, onError, settings);
  }, [settings.enableHighAccuracy, settings.timeout, settings.maximumAge]);

  return { ...position, error };
};
