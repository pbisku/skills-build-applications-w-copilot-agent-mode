import React, { useEffect, useState } from 'react';
import 'bootstrap/dist/css/bootstrap.min.css';

const Teams = () => {
    const [teams, setTeams] = useState([]);

    useEffect(() => {
        fetch('https://automatic-space-computing-machine-g75qxpvv5g2p647-8000.app.github.dev/api/teams')
            .then(response => response.json())
            .then(data => setTeams(data))
            .catch(error => console.error('Error fetching teams:', error));
    }, []);

    return (
        <div className="container mt-4">
            <h1 className="display-4 text-center">Teams</h1>
            <table className="table table-striped table-bordered mt-4">
                <thead className="thead-dark">
                    <tr>
                        <th>ID</th>
                        <th>Name</th>
                        <th>Members</th>
                    </tr>
                </thead>
                <tbody>
                    {teams.map(team => (
                        <tr key={team.id}>
                            <td>{team.id}</td>
                            <td>{team.name}</td>
                            <td>{team.members.join(', ')}</td>
                        </tr>
                    ))}
                </tbody>
            </table>
        </div>
    );
};

export default Teams;
