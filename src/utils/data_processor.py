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
    
    def _extract_values(self, data: List[dict]) -> List[float]:
        """Extract values from data items"""
        return [item.get('value', 0) for item in data]
    
    def calculate_metrics(self, data: List[dict]) -> dict:
        """Calculate metrics without code duplication"""
        if not data:
            return {'total': 0, 'average': 0, 'max': 0, 'min': 0}
        
        values = self._extract_values(data)
        
        return {
            'total': sum(values),
            'average': sum(values) / len(values),
            'max': max(values),
            'min': min(values)
        }
