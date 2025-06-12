import React from "react";
import UserSurvey from "./components/UserSurvey";

export default function App() {
  const handleComplete = (answers) => {
    console.log("Survey complete:", answers);
  };

  return (
    <div style={{ padding: 20 }}>
      <h1>Input Survey</h1>
      <UserSurvey onComplete={handleComplete} />
    </div>
  );
}