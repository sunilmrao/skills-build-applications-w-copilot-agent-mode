import React, { useEffect, useState } from 'react';

const API_URL = `https://${process.env.REACT_APP_CODESPACE_NAME}-8000.app.github.dev/api/activities/`;


function Activities() {
  const [activities, setActivities] = useState([]);

  useEffect(() => {
    fetch(API_URL)
      .then(res => res.json())
      .then(data => {
        const results = data.results || data;
        setActivities(results);
        console.log('Activities API:', API_URL);
        console.log('Fetched activities:', results);
      });
  }, []);

  return (
    <div className="container mt-4">
      <h2 className="mb-4 display-6">Activities</h2>
      <div className="card">
        <div className="card-body">
          <table className="table table-striped table-hover">
            <thead className="table-dark">
              <tr>
                <th>#</th>
                <th>User</th>
                <th>Workout</th>
                <th>Date</th>
                <th>Duration (min)</th>
              </tr>
            </thead>
            <tbody>
              {activities.map((activity, idx) => (
                <tr key={activity.id || idx}>
                  <td>{idx + 1}</td>
                  <td>{activity.user || ''}</td>
                  <td>{activity.workout || ''}</td>
                  <td>{activity.date || ''}</td>
                  <td>{activity.duration || ''}</td>
                </tr>
              ))}
            </tbody>
          </table>
        </div>
      </div>
    </div>
  );
}

export default Activities;
