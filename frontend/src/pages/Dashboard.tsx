import React, { useEffect, useState } from 'react';
import {
  Container,
  Grid,
  Paper,
  Typography,
  Box,
  AppBar,
  Toolbar,
  Button,
} from '@mui/material';
import { useNavigate } from 'react-router-dom';
import { alertsAPI, eventsAPI } from '../services/api';

const Dashboard: React.FC = () => {
  const navigate = useNavigate();
  const [stats, setStats] = useState({
    totalEvents: 0,
    totalAlerts: 0,
    criticalAlerts: 0,
  });

  useEffect(() => {
    loadStats();
  }, []);

  const loadStats = async () => {
    try {
      const [eventsData, alertsData] = await Promise.all([
        eventsAPI.getEvents({ page_size: 1 }),
        alertsAPI.getAlerts({ page_size: 1000 }),
      ]);
      
      setStats({
        totalEvents: eventsData.total || 0,
        totalAlerts: alertsData.total || 0,
        criticalAlerts: alertsData.alerts?.filter((a: any) => a.severity === 'CRITICAL').length || 0,
      });
    } catch (error) {
      console.error('Failed to load stats:', error);
    }
  };

  const handleLogout = () => {
    localStorage.removeItem('access_token');
    navigate('/login');
  };

  return (
    <Box sx={{ flexGrow: 1 }}>
      <AppBar position="static">
        <Toolbar>
          <Typography variant="h6" sx={{ flexGrow: 1 }}>
            Smart Retail Monitoring Platform
          </Typography>
          <Button color="inherit" onClick={() => navigate('/events')}>Events</Button>
          <Button color="inherit" onClick={() => navigate('/alerts')}>Alerts</Button>
          <Button color="inherit" onClick={() => navigate('/rules')}>Rules</Button>
          <Button color="inherit" onClick={handleLogout}>Logout</Button>
        </Toolbar>
      </AppBar>
      
      <Container maxWidth="lg" sx={{ mt: 4, mb: 4 }}>
        <Grid container spacing={3}>
          <Grid item xs={12} md={4}>
            <Paper sx={{ p: 3, display: 'flex', flexDirection: 'column', height: 140 }}>
              <Typography variant="h6" gutterBottom>
                Total Events
              </Typography>
              <Typography variant="h3" component="div" sx={{ flexGrow: 1 }}>
                {stats.totalEvents}
              </Typography>
            </Paper>
          </Grid>
          
          <Grid item xs={12} md={4}>
            <Paper sx={{ p: 3, display: 'flex', flexDirection: 'column', height: 140 }}>
              <Typography variant="h6" gutterBottom>
                Total Alerts
              </Typography>
              <Typography variant="h3" component="div" sx={{ flexGrow: 1 }}>
                {stats.totalAlerts}
              </Typography>
            </Paper>
          </Grid>
          
          <Grid item xs={12} md={4}>
            <Paper sx={{ p: 3, display: 'flex', flexDirection: 'column', height: 140 }}>
              <Typography variant="h6" gutterBottom color="error">
                Critical Alerts
              </Typography>
              <Typography variant="h3" component="div" sx={{ flexGrow: 1 }} color="error">
                {stats.criticalAlerts}
              </Typography>
            </Paper>
          </Grid>
        </Grid>
      </Container>
    </Box>
  );
};

export default Dashboard;
