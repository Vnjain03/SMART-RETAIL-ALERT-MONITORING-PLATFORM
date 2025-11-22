import React from 'react';
import { Container, Typography, Paper, Box } from '@mui/material';

const Alerts: React.FC = () => {
  return (
    <Container maxWidth="lg" sx={{ mt: 4 }}>
      <Paper sx={{ p: 3 }}>
        <Typography variant="h4" gutterBottom>
          Alerts
        </Typography>
        <Box sx={{ mt: 2 }}>
          <Typography color="textSecondary">
            Alert listing will appear here
          </Typography>
        </Box>
      </Paper>
    </Container>
  );
};

export default Alerts;
