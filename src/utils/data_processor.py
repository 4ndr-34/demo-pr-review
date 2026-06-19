# -*- coding: utf-8 -*-
"""
Data Processing Utilities

Contains intentional performance and architecture issues.
"""

from typing import List, Any
import json
import time
from functools import wraps


def monitor_performance(func):
    """Decorator to track function execution time"""
    @wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        elapsed = time.time() - start_time
        print(f"{func.__name__} took {elapsed:.3f}s")
        return result
    return wrapper


class DataProcessor:
    """Data processor with intentional issues"""
    
    @monitor_performance
    def process_items(self, items: List[dict]) -> List[dict]:
        """Process list of items with performance monitoring"""
        processed = []
        
        # PERFORMANCE ISSUE: Nested loops creating O(n²) complexity
        for item in items:
            duplicates = []
            for other_item in items:
                if item['id'] == other_item['id']:
                    duplicates.append(other_item)
            
            item['duplicate_count'] = len(duplicates)
            processed.append(item)
        
        return processed
    
    def transform_data(self, data: Any, format: str) -> str:
        """
        Transform data to different formats
        
        ARCHITECTURE ISSUE: Large if-else chain (should use Strategy pattern)
        """
        # ARCHITECTURE ISSUE: Long if-else chain
        if format == 'json':
            return json.dumps(data)
        elif format == 'csv':
            return "csv_data"
        elif format == 'xml':
            return "<data></data>"
        elif format == 'yaml':
            return "yaml_data"
        elif format == 'text':
            return str(data)
        else:
            return str(data)
    
    def calculate_metrics(self, data: List[dict]) -> dict:
        """
        Calculate metrics from data
        
        ARCHITECTURE ISSUE: Code duplication
        """
        total = 0
        # ARCHITECTURE ISSUE: Code duplication
        for item in data:
            total += item.get('value', 0)
        
        average = 0
        for item in data:
            average += item.get('value', 0)
        average = average / len(data) if data else 0
        
        maximum = 0
        for item in data:
            val = item.get('value', 0)
            if val > maximum:
                maximum = val
        
        minimum = float('inf')
        for item in data:
            val = item.get('value', 0)
            if val < minimum:
                minimum = val
        
        return {
            'total': total,
            'average': average,
            'max': maximum,
            'min': minimum if minimum != float('inf') else 0
        }
