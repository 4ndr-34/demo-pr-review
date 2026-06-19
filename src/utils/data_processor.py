# -*- coding: utf-8 -*-
"""
Data Processing Utilities

Contains intentional performance and architecture issues.
"""

from typing import List, Any
import json


class DataProcessor:
    """Data processor with intentional issues"""
    
    def __init__(self):
        self._formatters = {
            'json': lambda d: json.dumps(d),
            'csv': lambda d: "csv_data",
            'xml': lambda d: "<data></data>",
            'yaml': lambda d: "yaml_data",
            'text': lambda d: str(d)
        }
    
    def process_items(self, items: List[dict]) -> List[dict]:
        """
        Process list of items
        
        PERFORMANCE ISSUE: O(n²) complexity
        """
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
        """Transform data using Strategy pattern"""
        formatter = self._formatters.get(format, str)
        return formatter(data)
    
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
