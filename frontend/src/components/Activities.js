import React, { useEffect, useState } from 'react';
import 'bootstrap/dist/css/bootstrap.min.css';

const Activities = () => {
    const [activities, setActivities] = useState([]);

    useEffect(() => {
        fetch('https://automatic-space-computing-machine-g75qxpvv5g2p647-8000.app.github.dev/api/activities')
            .then(response => response.json())
            .then(data => setActivities(data))
            .catch(error => console.error('Error fetching activities:', error));
    }, []);

    return (
        <div className="container mt-4">
            <h1 className="display-4 text-center">Activities</h1>
            <table className="table table-striped table-bordered mt-4">
                <thead className="thead-dark">
                    <tr>
                        <th>ID</th>
                        <th>Name</th>
                    </tr>
                </thead>
                <tbody>
                    {activities.map(activity => (
                        <tr key={activity.id}>
                            <td>{activity.id}</td>
                            <td>{activity.name}</td>
                        </tr>
                    ))}
                </tbody>
            </table>
        </div>
    );
};

export default Activities;
