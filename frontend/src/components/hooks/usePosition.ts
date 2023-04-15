import { useState, useEffect } from "react";

const defaultSettings = {
  enableHighAccuracy: false,
  timeout: Infinity,
  maximumAge: 0,
};

interface IUsePosition {
  error: any;
  latitude?: number;
  longitude?: number;
}

export const usePosition = (watch = false, userSettings = {}): IUsePosition => {
  const settings = {
    ...defaultSettings,
    ...userSettings,
  };

  const [position, setPosition] = useState({ latitude: null, longitude: null });
  const [error, setError] = useState(null);

  const onChange = ({ coords, timestamp }) => {
    setPosition((prev) => {
      if (
        prev.latitude !== coords.latitude &&
        prev.longitude !== coords.longitude
      ) {
        return {
          latitude: coords.latitude,
          longitude: coords.longitude,
          // accuracy: coords.accuracy,
          // speed: coords.speed,
          // heading: coords.heading,
          // timestamp,
        };
      }
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
