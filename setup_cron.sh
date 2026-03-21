#!/bin/bash
# Setup automated maintenance scheduling for LovePDFs
# This script sets up cron jobs to run maintenance automatically

echo "🔧 Setting up automated maintenance for LovePDFs..."

# Create cron job for daily maintenance (runs at 2 AM)
echo "0 2 * * * cd /home/rameez/Downloads/ilovepdfs && python3 maintenance_scheduler.py" | crontab -

# Create cron job for weekly blog posts (runs every Sunday at 10 AM)
echo "0 10 * * 0 cd /home/rameez/Downloads/ilovepdfs && python3 blog_manager.py" | crontab -

# Add to existing crontab if it exists
(crontab -l 2>/dev/null; echo "0 2 * * * cd /home/rameez/Downloads/ilovepdfs && python3 maintenance_scheduler.py") | crontab -
(crontab -l 2>/dev/null; echo "0 10 * * 0 cd /home/rameez/Downloads/ilovepdfs && python3 blog_manager.py") | crontab -

echo "✅ Cron jobs created:"
echo "  - Daily maintenance at 2:00 AM"
echo "  - Weekly blog post creation at 10:00 AM on Sundays"

# Show current crontab
echo ""
echo "📅 Current cron jobs:"
crontab -l

echo ""
echo "💡 To manually run maintenance:"
echo "  cd /home/rameez/Downloads/ilovepdfs && python3 maintenance_scheduler.py"
