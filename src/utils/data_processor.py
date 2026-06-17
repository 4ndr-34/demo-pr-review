# -*- coding: utf-8 -*-
"""
Data Processing Utilities

Contains intentional performance and architecture issues.
"""

from typing import List, Any
import json


class DataProcessor:
    """Data processor with intentional issues"""
    
    def process_items(self, items: List[dict]) -> List[dict]:
        """
        Process list of items
        
        Fixed: Using dictionary for O(n) complexity
        """
        processed = []
        
        # FIXED: Using dictionary to count duplicates in O(n) time
        id_counts = {}
        for item in items:
            item_id = item['id']
            id_counts[item_id] = id_counts.get(item_id, 0) + 1
        
        for item in items:
            item['duplicate_count'] = id_counts[item['id']]
            processed.append(item)
        
        return processed
    
    def cache_heavy_computation(self, data: List[dict]) -> dict:
        """
        Cache results of heavy computation
        
        NEW METHOD: Added caching for expensive operations
        """
        # PERFORMANCE ISSUE: Memory leak - cache never cleared
        if not hasattr(self, '_cache'):
            self._cache = {}
        
        cache_key = str(data)
        
        if cache_key in self._cache:
            return self._cache[cache_key]
        
        # Expensive computation
        result = {
            'processed_count': len(data),
            'total_value': sum(item.get('value', 0) for item in data)
        }
        
        # ISSUE: Cache grows unbounded, potential memory leak
        self._cache[cache_key] = result
        
        return result
    
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
