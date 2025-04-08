import React, { useEffect, useState } from 'react';
import 'bootstrap/dist/css/bootstrap.min.css';

const Leaderboard = () => {
    const [leaders, setLeaders] = useState([]);

    useEffect(() => {
        fetch('https://automatic-space-computing-machine-g75qxpvv5g2p647-8000.app.github.dev/api/leaderboard')
            .then(response => response.json())
            .then(data => setLeaders(data))
            .catch(error => console.error('Error fetching leaderboard:', error));
    }, []);

    return (
        <div className="container mt-4">
            <h1 className="display-4 text-center">Leaderboard</h1>
            <table className="table table-striped table-bordered mt-4">
                <thead className="thead-dark">
                    <tr>
                        <th>Rank</th>
                        <th>Name</th>
                        <th>Score</th>
                    </tr>
                </thead>
                <tbody>
                    {leaders.map((leader, index) => (
                        <tr key={leader.id}>
                            <td>{index + 1}</td>
                            <td>{leader.name}</td>
                            <td>{leader.score}</td>
                        </tr>
                    ))}
                </tbody>
            </table>
        </div>
    );
};

export default Leaderboard;
