export interface Event {
  id: string;
  service: string;
  timestamp: number;
  latency_ms?: number;
  error_code?: string;
  status: 'OK' | 'ERROR' | 'WARNING';
  metadata?: Record<string, any>;
}

export interface Alert {
  id: string;
  service: string;
  rule_id: string;
  severity: 'LOW' | 'MEDIUM' | 'HIGH' | 'CRITICAL';
  message: string;
  timestamp: number;
  acknowledged: boolean;
  acknowledged_by?: string;
  acknowledged_at?: number;
}

export interface Rule {
  id: string;
  service: string;
  name: string;
  type: 'THRESHOLD' | 'RATE' | 'ANOMALY';
  condition: RuleCondition;
  severity: string;
  enabled: boolean;
  description?: string;
  created_at: number;
}

export interface RuleCondition {
  metric: string;
  operator: string;
  value: number;
  consecutive_events?: number;
  time_window_seconds?: number;
  threshold_std_dev?: number;
  lookback_minutes?: number;
}

export interface User {
  id: string;
  email: string;
  full_name?: string;
  role: string;
  is_active: boolean;
  created_at: number;
}

export interface LoginCredentials {
  email: string;
  password: string;
}

export interface AuthToken {
  access_token: string;
  token_type: string;
  expires_in: number;
}
