import React from 'react';
import { Container, Typography, Paper, Box } from '@mui/material';

const Rules: React.FC = () => {
  return (
    <Container maxWidth="lg" sx={{ mt: 4 }}>
      <Paper sx={{ p: 3 }}>
        <Typography variant="h4" gutterBottom>
          Alert Rules
        </Typography>
        <Box sx={{ mt: 2 }}>
          <Typography color="textSecondary">
            Rule management interface will appear here
          </Typography>
        </Box>
      </Paper>
    </Container>
  );
};

export default Rules;
