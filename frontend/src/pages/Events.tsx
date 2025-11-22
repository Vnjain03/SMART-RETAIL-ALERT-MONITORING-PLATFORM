import React from 'react';
import { Container, Typography, Paper, Box } from '@mui/material';

const Events: React.FC = () => {
  return (
    <Container maxWidth="lg" sx={{ mt: 4 }}>
      <Paper sx={{ p: 3 }}>
        <Typography variant="h4" gutterBottom>
          Events
        </Typography>
        <Box sx={{ mt: 2 }}>
          <Typography color="textSecondary">
            Event listing will appear here
          </Typography>
        </Box>
      </Paper>
    </Container>
  );
};

export default Events;
